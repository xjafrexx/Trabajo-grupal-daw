import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { libraryApi } from '../api/libraryApi'

export function useCategories() {
  return useQuery({
    queryKey: ['categories', 'list'],
    queryFn: () => libraryApi.getCategories(),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCategoryDetail(id: string) {
  return useQuery({
    queryKey: ['categories', 'detail', id],
    queryFn: () => libraryApi.getCategory(id),
    enabled: Boolean(id),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCreateCategory() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.createCategory,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories', 'list'] })
    },
  })
}

export function useUpdateCategory() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Parameters<typeof libraryApi.updateCategory>[1] }) => 
      libraryApi.updateCategory(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories', 'list'] })
    },
  })
}

export function useDeleteCategory() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.deleteCategory,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories', 'list'] })
    },
  })
}