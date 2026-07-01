import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { libraryApi } from '../api/libraryApi'

export function useUsers() {
  return useQuery({
    queryKey: ['users', 'list'],
    queryFn: () => libraryApi.getUsers(),
    staleTime: 1000 * 60 * 10,
  })
}

export function useLoans() {
  return useQuery({
    queryKey: ['loans', 'list'],
    queryFn: () => libraryApi.getLoans(),
    staleTime: 1000 * 60 * 5,
  })
}

export function useLoanDetail(id: string) {
  return useQuery({
    queryKey: ['loans', 'detail', id],
    queryFn: () => libraryApi.getLoan(id),
    enabled: Boolean(id),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCreateLoan() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.createLoan,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['loans', 'list'] })
      queryClient.invalidateQueries({ queryKey: ['book-copies'] })
    },
  })
}

export function useUpdateLoan() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Parameters<typeof libraryApi.updateLoan>[1] }) => 
      libraryApi.updateLoan(id, data),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['loans', 'list'] })
      queryClient.invalidateQueries({ queryKey: ['loans', 'detail', variables.id] })
      queryClient.invalidateQueries({ queryKey: ['book-copies'] })
    },
  })
}

export function useDeleteLoan() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.deleteLoan,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['loans', 'list'] })
    },
  })
}