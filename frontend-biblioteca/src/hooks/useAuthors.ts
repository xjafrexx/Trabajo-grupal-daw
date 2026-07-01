import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { libraryApi } from '../api/libraryApi'

export function useAuthors() {
  return useQuery({
    queryKey: ['authors', 'list'],
    queryFn: () => libraryApi.getAuthors(),
    staleTime: 1000 * 60 * 5,
  })
}

export function useAuthorDetail(id: string) {
  return useQuery({
    queryKey: ['authors', 'detail', id],
    queryFn: () => libraryApi.getAuthor(id),
    enabled: Boolean(id),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCreateAuthor() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.createAuthor,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['authors', 'list'] })
    },
  })
}

export function useUpdateAuthor() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Parameters<typeof libraryApi.updateAuthor>[1] }) => 
      libraryApi.updateAuthor(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['authors', 'list'] })
    },
  })
}

export function useDeleteAuthor() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.deleteAuthor,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['authors', 'list'] })
    },
  })
}